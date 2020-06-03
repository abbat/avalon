#!/usr/bin/env bash

set -e

# имя проекта
PROJECT_NAME="avalon"

# версия qt
if [ -z "${QT_SELECT}" ]; then
	export QT_SELECT=4
elif [ "${QT_SELECT}" != "4" ]; then
	echo "Build require Qt 4.x only :("
	exit
fi

# очистка
if [ -f "Makefile" ]; then
	make clean
fi

# создание pro-файла
BUILD_DIR=$(pwd)
qmake -project -recursive -Wall -nopwd -o ${PROJECT_NAME}.pro \
    "CONFIG      += debug_and_release"                        \
    "QT          += network sql webkit"                       \
    "INCLUDEPATH += src"                                      \
    "LIBS        += -laspell -lz"                             \
    "macx { QMAKE_CXX = clang }"                              \
    "macx { ICON = icons/avalon.icns }"                       \
    "${BUILD_DIR}/src"

# создание make-файлов
qmake ${PROJECT_NAME}.pro

# создание бинарника
make $1

# удаление символов
strip -s ${PROJECT_NAME}

# запуск
if [ -z "${TRAVIS}" ]; then
	./${PROJECT_NAME}
fi
