#!/usr/local/bin/python3
from PyQt5.QtWidgets import QWidget, QTextEdit, QSplitter, QVBoxLayout
from PyQt5.QtCore import Qt
from streaming import StreamingThread
from text_edit_read_write import reader, writer


class StreamEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.__th = StreamingThread()
        self.__final_result_viewer = QTextEdit()
        self.__all_result_viewer = QTextEdit()

        self.__set_layout()

    def __set_layout(self):
        v_box = QVBoxLayout()
        splitter = QSplitter(Qt.Vertical)
        self.__final_result_viewer.setReadOnly(True)
        self.__final_result_viewer.append("[音声認識結果の最終文]")
        self.__all_result_viewer.setReadOnly(False)
        self.__all_result_viewer.append("[音声認識の逐次結果]")

        splitter.addWidget(self.__final_result_viewer)
        splitter.addWidget(self.__all_result_viewer)

        v_box.addWidget(splitter)
        self.setLayout(v_box)

    def run_streaming_thread(self):
        self.__th.streaming_result.connect(self.__all_result_viewer.append)
        self.__th.final_result.connect(self.__final_result_viewer.append)
        self.__th.start()

    def read_final_result(self, file):
        reader(file, self.__final_result_viewer)

    def write_final_result(self, file):
        writer(file, self.__final_result_viewer)