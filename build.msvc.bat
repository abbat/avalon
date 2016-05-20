@ECHO OFF

REM ***************
REM * ��� ������� *
REM ***************
SET PROJECT_NAME=avalon

REM **************************
REM * ����������� ���� qmake *
REM **************************
SET QT_QMAKE=c:\projects\qt\bin\qmake.exe

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
SET ZLIB_LIB=c:\projects\zlib\lib\static32\zlibstat.lib
SET ZLIB_INC=c:\projects\zlib\include

REM *******************************
REM * �������� ������� � makefile *
REM *******************************
%QT_QMAKE% -project -recursive -Wall -nopwd -o %PROJECT_NAME%.pro "CONFIG += release" "QT += network sql webkit" "INCLUDEPATH += %ASPELL_INC% %ZLIB_INC% src" "LIBS += %ASPELL_LIB% %ZLIB_LIB%" "RC_FILE += src/resource.rc" src
%QT_QMAKE% %PROJECT_NAME%.pro

REM ******************************************
REM * ������ (������� ������ ���� �������� � *
REM * Visual Studio 2005 Command Prompt)     *
REM ******************************************
nmake.exe
