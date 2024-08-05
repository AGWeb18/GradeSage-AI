# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/Element.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from streamlit.proto import Alert_pb2 as streamlit_dot_proto_dot_Alert__pb2
from streamlit.proto import Arrow_pb2 as streamlit_dot_proto_dot_Arrow__pb2
from streamlit.proto import Audio_pb2 as streamlit_dot_proto_dot_Audio__pb2
from streamlit.proto import Balloons_pb2 as streamlit_dot_proto_dot_Balloons__pb2
from streamlit.proto import ArrowVegaLiteChart_pb2 as streamlit_dot_proto_dot_ArrowVegaLiteChart__pb2
from streamlit.proto import BokehChart_pb2 as streamlit_dot_proto_dot_BokehChart__pb2
from streamlit.proto import Button_pb2 as streamlit_dot_proto_dot_Button__pb2
from streamlit.proto import ButtonGroup_pb2 as streamlit_dot_proto_dot_ButtonGroup__pb2
from streamlit.proto import DownloadButton_pb2 as streamlit_dot_proto_dot_DownloadButton__pb2
from streamlit.proto import CameraInput_pb2 as streamlit_dot_proto_dot_CameraInput__pb2
from streamlit.proto import ChatInput_pb2 as streamlit_dot_proto_dot_ChatInput__pb2
from streamlit.proto import Checkbox_pb2 as streamlit_dot_proto_dot_Checkbox__pb2
from streamlit.proto import Code_pb2 as streamlit_dot_proto_dot_Code__pb2
from streamlit.proto import ColorPicker_pb2 as streamlit_dot_proto_dot_ColorPicker__pb2
from streamlit.proto import DataFrame_pb2 as streamlit_dot_proto_dot_DataFrame__pb2
from streamlit.proto import DateInput_pb2 as streamlit_dot_proto_dot_DateInput__pb2
from streamlit.proto import DeckGlJsonChart_pb2 as streamlit_dot_proto_dot_DeckGlJsonChart__pb2
from streamlit.proto import DocString_pb2 as streamlit_dot_proto_dot_DocString__pb2
from streamlit.proto import Empty_pb2 as streamlit_dot_proto_dot_Empty__pb2
from streamlit.proto import Exception_pb2 as streamlit_dot_proto_dot_Exception__pb2
from streamlit.proto import Favicon_pb2 as streamlit_dot_proto_dot_Favicon__pb2
from streamlit.proto import FileUploader_pb2 as streamlit_dot_proto_dot_FileUploader__pb2
from streamlit.proto import GraphVizChart_pb2 as streamlit_dot_proto_dot_GraphVizChart__pb2
from streamlit.proto import Html_pb2 as streamlit_dot_proto_dot_Html__pb2
from streamlit.proto import IFrame_pb2 as streamlit_dot_proto_dot_IFrame__pb2
from streamlit.proto import Image_pb2 as streamlit_dot_proto_dot_Image__pb2
from streamlit.proto import Json_pb2 as streamlit_dot_proto_dot_Json__pb2
from streamlit.proto import LinkButton_pb2 as streamlit_dot_proto_dot_LinkButton__pb2
from streamlit.proto import NumberInput_pb2 as streamlit_dot_proto_dot_NumberInput__pb2
from streamlit.proto import Markdown_pb2 as streamlit_dot_proto_dot_Markdown__pb2
from streamlit.proto import Metric_pb2 as streamlit_dot_proto_dot_Metric__pb2
from streamlit.proto import MultiSelect_pb2 as streamlit_dot_proto_dot_MultiSelect__pb2
from streamlit.proto import PageLink_pb2 as streamlit_dot_proto_dot_PageLink__pb2
from streamlit.proto import PlotlyChart_pb2 as streamlit_dot_proto_dot_PlotlyChart__pb2
from streamlit.proto import Components_pb2 as streamlit_dot_proto_dot_Components__pb2
from streamlit.proto import Progress_pb2 as streamlit_dot_proto_dot_Progress__pb2
from streamlit.proto import Snow_pb2 as streamlit_dot_proto_dot_Snow__pb2
from streamlit.proto import Spinner_pb2 as streamlit_dot_proto_dot_Spinner__pb2
from streamlit.proto import Radio_pb2 as streamlit_dot_proto_dot_Radio__pb2
from streamlit.proto import Selectbox_pb2 as streamlit_dot_proto_dot_Selectbox__pb2
from streamlit.proto import Skeleton_pb2 as streamlit_dot_proto_dot_Skeleton__pb2
from streamlit.proto import Slider_pb2 as streamlit_dot_proto_dot_Slider__pb2
from streamlit.proto import Text_pb2 as streamlit_dot_proto_dot_Text__pb2
from streamlit.proto import TextArea_pb2 as streamlit_dot_proto_dot_TextArea__pb2
from streamlit.proto import TextInput_pb2 as streamlit_dot_proto_dot_TextInput__pb2
from streamlit.proto import TimeInput_pb2 as streamlit_dot_proto_dot_TimeInput__pb2
from streamlit.proto import Toast_pb2 as streamlit_dot_proto_dot_Toast__pb2
from streamlit.proto import VegaLiteChart_pb2 as streamlit_dot_proto_dot_VegaLiteChart__pb2
from streamlit.proto import Video_pb2 as streamlit_dot_proto_dot_Video__pb2
from streamlit.proto import Heading_pb2 as streamlit_dot_proto_dot_Heading__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dstreamlit/proto/Element.proto\x1a\x1bstreamlit/proto/Alert.proto\x1a\x1bstreamlit/proto/Arrow.proto\x1a\x1bstreamlit/proto/Audio.proto\x1a\x1estreamlit/proto/Balloons.proto\x1a(streamlit/proto/ArrowVegaLiteChart.proto\x1a streamlit/proto/BokehChart.proto\x1a\x1cstreamlit/proto/Button.proto\x1a!streamlit/proto/ButtonGroup.proto\x1a$streamlit/proto/DownloadButton.proto\x1a!streamlit/proto/CameraInput.proto\x1a\x1fstreamlit/proto/ChatInput.proto\x1a\x1estreamlit/proto/Checkbox.proto\x1a\x1astreamlit/proto/Code.proto\x1a!streamlit/proto/ColorPicker.proto\x1a\x1fstreamlit/proto/DataFrame.proto\x1a\x1fstreamlit/proto/DateInput.proto\x1a%streamlit/proto/DeckGlJsonChart.proto\x1a\x1fstreamlit/proto/DocString.proto\x1a\x1bstreamlit/proto/Empty.proto\x1a\x1fstreamlit/proto/Exception.proto\x1a\x1dstreamlit/proto/Favicon.proto\x1a\"streamlit/proto/FileUploader.proto\x1a#streamlit/proto/GraphVizChart.proto\x1a\x1astreamlit/proto/Html.proto\x1a\x1cstreamlit/proto/IFrame.proto\x1a\x1bstreamlit/proto/Image.proto\x1a\x1astreamlit/proto/Json.proto\x1a streamlit/proto/LinkButton.proto\x1a!streamlit/proto/NumberInput.proto\x1a\x1estreamlit/proto/Markdown.proto\x1a\x1cstreamlit/proto/Metric.proto\x1a!streamlit/proto/MultiSelect.proto\x1a\x1estreamlit/proto/PageLink.proto\x1a!streamlit/proto/PlotlyChart.proto\x1a streamlit/proto/Components.proto\x1a\x1estreamlit/proto/Progress.proto\x1a\x1astreamlit/proto/Snow.proto\x1a\x1dstreamlit/proto/Spinner.proto\x1a\x1bstreamlit/proto/Radio.proto\x1a\x1fstreamlit/proto/Selectbox.proto\x1a\x1estreamlit/proto/Skeleton.proto\x1a\x1cstreamlit/proto/Slider.proto\x1a\x1astreamlit/proto/Text.proto\x1a\x1estreamlit/proto/TextArea.proto\x1a\x1fstreamlit/proto/TextInput.proto\x1a\x1fstreamlit/proto/TimeInput.proto\x1a\x1bstreamlit/proto/Toast.proto\x1a#streamlit/proto/VegaLiteChart.proto\x1a\x1bstreamlit/proto/Video.proto\x1a\x1dstreamlit/proto/Heading.proto\"\xb4\r\n\x07\x45lement\x12\x17\n\x05\x61lert\x18\x1e \x01(\x0b\x32\x06.AlertH\x00\x12\"\n\x10\x61rrow_data_frame\x18( \x01(\x0b\x32\x06.ArrowH\x00\x12\x1d\n\x0b\x61rrow_table\x18\' \x01(\x0b\x32\x06.ArrowH\x00\x12\x34\n\x15\x61rrow_vega_lite_chart\x18) \x01(\x0b\x32\x13.ArrowVegaLiteChartH\x00\x12\x17\n\x05\x61udio\x18\r \x01(\x0b\x32\x06.AudioH\x00\x12\x1d\n\x08\x62\x61lloons\x18\x0c \x01(\x0b\x32\t.BalloonsH\x00\x12\"\n\x0b\x62okeh_chart\x18\x11 \x01(\x0b\x32\x0b.BokehChartH\x00\x12\x19\n\x06\x62utton\x18\x13 \x01(\x0b\x32\x07.ButtonH\x00\x12$\n\x0c\x62utton_group\x18\x37 \x01(\x0b\x32\x0c.ButtonGroupH\x00\x12*\n\x0f\x64ownload_button\x18+ \x01(\x0b\x32\x0f.DownloadButtonH\x00\x12$\n\x0c\x63\x61mera_input\x18- \x01(\x0b\x32\x0c.CameraInputH\x00\x12 \n\nchat_input\x18\x31 \x01(\x0b\x32\n.ChatInputH\x00\x12\x1d\n\x08\x63heckbox\x18\x14 \x01(\x0b\x32\t.CheckboxH\x00\x12$\n\x0c\x63olor_picker\x18# \x01(\x0b\x32\x0c.ColorPickerH\x00\x12\x30\n\x12\x63omponent_instance\x18% \x01(\x0b\x32\x12.ComponentInstanceH\x00\x12 \n\ndata_frame\x18\x03 \x01(\x0b\x32\n.DataFrameH\x00\x12\x1b\n\x05table\x18\x0b \x01(\x0b\x32\n.DataFrameH\x00\x12 \n\ndate_input\x18\x1b \x01(\x0b\x32\n.DateInputH\x00\x12.\n\x12\x64\x65\x63k_gl_json_chart\x18\" \x01(\x0b\x32\x10.DeckGlJsonChartH\x00\x12 \n\ndoc_string\x18\x07 \x01(\x0b\x32\n.DocStringH\x00\x12\x17\n\x05\x65mpty\x18\x02 \x01(\x0b\x32\x06.EmptyH\x00\x12\x1f\n\texception\x18\x08 \x01(\x0b\x32\n.ExceptionH\x00\x12\x1b\n\x07\x66\x61vicon\x18$ \x01(\x0b\x32\x08.FaviconH\x00\x12&\n\rfile_uploader\x18! \x01(\x0b\x32\r.FileUploaderH\x00\x12(\n\x0egraphviz_chart\x18\x12 \x01(\x0b\x32\x0e.GraphVizChartH\x00\x12\x15\n\x04html\x18\x36 \x01(\x0b\x32\x05.HtmlH\x00\x12\x19\n\x06iframe\x18& \x01(\x0b\x32\x07.IFrameH\x00\x12\x1a\n\x04imgs\x18\x06 \x01(\x0b\x32\n.ImageListH\x00\x12\x15\n\x04json\x18\x1f \x01(\x0b\x32\x05.JsonH\x00\x12\"\n\x0blink_button\x18\x33 \x01(\x0b\x32\x0b.LinkButtonH\x00\x12\x1d\n\x08markdown\x18\x1d \x01(\x0b\x32\t.MarkdownH\x00\x12\x19\n\x06metric\x18* \x01(\x0b\x32\x07.MetricH\x00\x12#\n\x0bmultiselect\x18\x1c \x01(\x0b\x32\x0c.MultiSelectH\x00\x12$\n\x0cnumber_input\x18  \x01(\x0b\x32\x0c.NumberInputH\x00\x12\x1e\n\tpage_link\x18\x35 \x01(\x0b\x32\t.PageLinkH\x00\x12$\n\x0cplotly_chart\x18\x10 \x01(\x0b\x32\x0c.PlotlyChartH\x00\x12\x1d\n\x08progress\x18\x05 \x01(\x0b\x32\t.ProgressH\x00\x12\x17\n\x05radio\x18\x17 \x01(\x0b\x32\x06.RadioH\x00\x12\x1f\n\tselectbox\x18\x19 \x01(\x0b\x32\n.SelectboxH\x00\x12\x1d\n\x08skeleton\x18\x34 \x01(\x0b\x32\t.SkeletonH\x00\x12\x19\n\x06slider\x18\x15 \x01(\x0b\x32\x07.SliderH\x00\x12\x15\n\x04snow\x18. \x01(\x0b\x32\x05.SnowH\x00\x12\x1b\n\x07spinner\x18, \x01(\x0b\x32\x08.SpinnerH\x00\x12\x15\n\x04text\x18\x01 \x01(\x0b\x32\x05.TextH\x00\x12\x1e\n\ttext_area\x18\x16 \x01(\x0b\x32\t.TextAreaH\x00\x12 \n\ntext_input\x18\x18 \x01(\x0b\x32\n.TextInputH\x00\x12 \n\ntime_input\x18\x1a \x01(\x0b\x32\n.TimeInputH\x00\x12\x17\n\x05toast\x18\x32 \x01(\x0b\x32\x06.ToastH\x00\x12)\n\x0fvega_lite_chart\x18\n \x01(\x0b\x32\x0e.VegaLiteChartH\x00\x12\x17\n\x05video\x18\x0e \x01(\x0b\x32\x06.VideoH\x00\x12\x1b\n\x07heading\x18/ \x01(\x0b\x32\x08.HeadingH\x00\x12\x15\n\x04\x63ode\x18\x30 \x01(\x0b\x32\x05.CodeH\x00\x42\x06\n\x04typeJ\x04\x08\t\x10\nB,\n\x1c\x63om.snowflake.apps.streamlitB\x0c\x45lementProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'streamlit.proto.Element_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.snowflake.apps.streamlitB\014ElementProto'
  _globals['_ELEMENT']._serialized_start=1648
  _globals['_ELEMENT']._serialized_end=3364
# @@protoc_insertion_point(module_scope)
