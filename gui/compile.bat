pyuic5 -x MainWindow.ui -o mainwindow_ui.py & ^
pyuic5 -x ModelConfig.ui -o modelconfig_ui.py & ^
pyuic5 -x SingleAnalyzer.ui -o singleanalyzer_ui.py & ^
pyuic5 -x MultipleAnalyzer.ui -o multipleanalyzer_ui.py & ^
pyuic5 -x ModelTest.ui -o modeltest_ui.py & ^
pyrcc5 source.qrc -o source_rc.py