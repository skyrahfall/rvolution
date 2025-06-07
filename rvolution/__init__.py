__title__ = "rvolution"
__license__ = "MIT"
__version__ = "0.2.1"

import requests
import re
import logging
from .defaults import COMMAND_CODES, DEFAULT_MEDIA_TITLE


BASE_COMMAND_URL_FORMAT = "http://{}/cgi-bin/do"
BASE_RVIDEO_URL_FORMAT = "http://{}:8990/{}"
STATE_PARSER = re.compile('.*name="(.*)" value="(.*)"')
TIMEOUT = 5
DEBUG = True
VALID_ENDPOINTS = ["IsAlive","LastMedia"]


class RVolutionPlayer():
	_address: str = ""
	_player_state: str = "init"
	_player_name: str = "NA"
	_current_file: str = ""
	_last_media: object = {}
	_rvideo_state: str = "unknown"

	def __init__(self, address):
		self._address = address
		self.update_state()
	def update_state(self):
		state = self.__send_command('status')
		if state.get('playback_url'):
			state['playback_url'] = state['playback_url'].encode('latin1').decode('utf8')
			filparts = state['playback_url'].split("/")
			self._current_file = filparts.pop()
		else:
			self._current_file = "none"
		if state.get("product_name"):
			self._player_name=state["product_name"]
		if state.get("product_state"):
			self._player_state=state["product_state"]
		
		self.__rvideo_api('IsAlive')
		self.__rvideo_api('LastMedia')
		return state
	def __parse_status(self, status):
		statuses = STATE_PARSER.findall(status)
		self._lastState = { val[0]: val[1] for val in statuses }
		if DEBUG:
			for val in statuses:
				logging.debug("{}\t:{}".format(val[0], val[1]) )
		return self._lastState
	def __parse_rvideo(self, status):
			self._rvideo_state = status.get('ErrorCode','undefined')
			self._last_media = status.get('Media',DEFAULT_MEDIA_TITLE)
			return True
	def __send_ir_code(self, code):
		self.__send_command('ir_code', { 'ir_code': code })
		return self.update_state()
	def send_button(self,button):
		ir_code = COMMAND_CODES.get(button)
		if ir_code != None:
			return self.__send_ir_code(ir_code)
		else:
			return {"error": "unknown button"}
	def supported_buttons(self):
		cmds = COMMAND_CODES.keys()
		return cmds
	def play_file(self, file):
		# file from internal drive: "file:///tmp/mnt/storage/R_volutionHDD_################/Filme/Back to the Future Part III.mkv"
		return self.__send_command("start_file_playback",{"media_url":file})
	# not support
	# def set_text(self, text):
	# 	return self.__send_command("set_text",{"text":text})
	# def get_text(self):
	# 	return self.__send_command("get_text")
	def __rvideo_api(self, endpoint):
		if endpoint not in VALID_ENDPOINTS:
			raise ValueError(f"'{endpoint}' not a valid endpoint")
		try:
			r = requests.get(
				BASE_RVIDEO_URL_FORMAT.format(self._address, endpoint),
				timeout = TIMEOUT
				)
		except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
			return {}

		if r.status_code == 200:
			rStatus = self.__parse_rvideo(r.json())
			# if "command_status" in tStatus and tStatus["command_status"] == "ok":
			logging.warning(rStatus)
			return rStatus
		else:
			return {}
	def __send_command(self, cmd, params = {}):
		params["cmd"] = cmd
		try:
			r = requests.get(
				BASE_COMMAND_URL_FORMAT.format(self._address),
				params = params,
				timeout = TIMEOUT
				)
		except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
			return {}

		if r.status_code == 200:
			tStatus = self.__parse_status(r.text)
			if "command_status" in tStatus and tStatus["command_status"] == "ok":
				logging.warning('cmd ok')
			return tStatus
		else:
			return {}