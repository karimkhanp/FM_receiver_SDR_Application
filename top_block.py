#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Fri May  3 00:17:14 2013
##################################################

from gnuradio import audio
from gnuradio import blks2
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Top Block")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.volume = volume = .05
		self.samp_rate = samp_rate = 32000
		self.resamp_factor = resamp_factor = 4

		##################################################
		# Blocks
		##################################################
		_volume_sizer = wx.BoxSizer(wx.VERTICAL)
		self._volume_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_volume_sizer,
			value=self.volume,
			callback=self.set_volume,
			label='volume',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._volume_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_volume_sizer,
			value=self.volume,
			callback=self.set_volume,
			minimum=0,
			maximum=0.1,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_volume_sizer)
		self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
			self.GetWin(),
			title="Scope Plot",
			sample_rate=256000,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=1,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
		)
		self.Add(self.wxgui_scopesink2_0.win)
		self.low_pass_filter_0 = gr.fir_filter_ccf(1, firdes.low_pass(
			1, 64000, 5000, 100, firdes.WIN_HAMMING, 6.76))
		self.gr_multiply_const_vxx_0 = gr.multiply_const_vff((volume, ))
		self.gr_file_source_1 = gr.file_source(gr.sizeof_gr_complex*1, "/media/technoworld/Study & SW/2nd SEM/Seminar/IMPLEMENTATION/am_usrp710.dat", True)
		self.gr_complex_to_mag_0 = gr.complex_to_mag(1)
		self.blks2_rational_resampler_xxx_0_0 = blks2.rational_resampler_fff(
			interpolation=3,
			decimation=resamp_factor,
			taps=None,
			fractional_bw=None,
		)
		self.blks2_rational_resampler_xxx_0 = blks2.rational_resampler_ccc(
			interpolation=1,
			decimation=resamp_factor,
			taps=None,
			fractional_bw=None,
		)
		self.audio_sink_0 = audio.sink(48000, "", True)

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_file_source_1, 0), (self.blks2_rational_resampler_xxx_0, 0))
		self.connect((self.low_pass_filter_0, 0), (self.gr_complex_to_mag_0, 0))
		self.connect((self.blks2_rational_resampler_xxx_0_0, 0), (self.audio_sink_0, 0))
		self.connect((self.blks2_rational_resampler_xxx_0_0, 0), (self.wxgui_scopesink2_0, 0))
		self.connect((self.gr_complex_to_mag_0, 0), (self.gr_multiply_const_vxx_0, 0))
		self.connect((self.gr_multiply_const_vxx_0, 0), (self.blks2_rational_resampler_xxx_0_0, 0))
		self.connect((self.blks2_rational_resampler_xxx_0, 0), (self.low_pass_filter_0, 0))

	def get_volume(self):
		return self.volume

	def set_volume(self, volume):
		self.volume = volume
		self._volume_slider.set_value(self.volume)
		self._volume_text_box.set_value(self.volume)
		self.gr_multiply_const_vxx_0.set_k((self.volume, ))

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate

	def get_resamp_factor(self):
		return self.resamp_factor

	def set_resamp_factor(self, resamp_factor):
		self.resamp_factor = resamp_factor

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

