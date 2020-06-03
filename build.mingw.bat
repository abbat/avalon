@ECHO OFF

REM ***************
REM * ��� ������� *
REM ***************
SET PROJECT_NAME=avalon

REM **************************
REM * ����������� ���� qmake *
REM **************************
SET QT_QMAKE=c:\projects\qt5\5.5\mingw492_32\bin\qmake.exe

REM **************************************************
REM * ���� � ������������ ������ � ���������� aspell *
REM * �������� ��������: http://aspell.net/win32/    *
REM **************************************************
SET ASPELL_INC=c:\projects\aspell\include
SET ASPELL_LIB=c:\projects\aspell\lib\aspell-15.lib

REM *****************************************************************
REM * ���� � ������������ ������ � ���������� zlib (�������)        *
REM * �������� ��������: http://www.winimage.com/zLibDll/index.html *
REM *****************************************************************
SET ZLIB_LIB=C:\projects\zlib128\lib\zdll.lib
SET ZLIB_INC=C:\projects\zlib128\include

REM *******************************
REM * �������� ������� � makefile *
REM *******************************
%QT_QMAKE% -project -recursive -Wall -nopwd -o %PROJECT_NAME%.pro "CONFIG += release" "QT += core network sql widgets webkitwidgets" "INCLUDEPATH += %ASPELL_INC% %ZLIB_INC% src" "LIBS += %ASPELL_LIB% %ZLIB_LIB%" "RC_FILE += src/resource.rc" %cd%/src/*
%QT_QMAKE% %PROJECT_NAME%.pro

REM ******************************************
REM * ������ (������� ������ ���� �������� � *
REM * Qt Command Prompt)                     *
REM ******************************************
mingw32-make.exe
