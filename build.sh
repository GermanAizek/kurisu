#!/bin/bash
set -e

MODELS_DIR="models"

whiptail --title "Setting up project - Kurisu" --msgbox \
 "`figlet Kurisu` Hey, to start working with me, you need to setup me.\nI wish you good fun." \
          15 36 0

MENUSTR="Plase select build option"
OPTION=$(whiptail --title "Setting up project - Kurisu" \
    --menu "$MENUSTR" 10 50 3 --cancel-button Finish --ok-button Select \
    "0"   "Download locale training models" \
    3>&1 1>&2 2>&3)

BOARD=$(whiptail --title "Setting up project - Kurisu" \
	--menu "$MENUSTR" 24 74 18 --cancel-button Finish --ok-button Select \
	"0"   "Generic US English 1.4G (vosk-model-en-us-aspire-0.2)" \
	"1"   "Lightweight US English 36M (vosk-model-small-en-us-0.3)" \
	"2"   "Accurate US English 3.2G (vosk-model-en-us-daanzu)" \
	"3"   "Config graph US English 129M (vosk-model-en-us-daanzu-lgraph)" \
	"4"   "Repackaged Kaldi US English 845M (vosk-model-en-us-librispeech-0.2)" \
	"5"   "Generic Russian 2.5G (vosk-model-ru-0.10)" \
	"6"   "Lightweight Russian 39M (vosk-model-small-ru-0.4)" \
	"7"   "Generic Chinese 195M (vosk-model-cn-0.1)" \
	"8"   "Lightweight Chinese 32M (vosk-model-small-cn-0.3)" \
	"9"   "Generic German 566M (tuda-de)" \
	"10"  "Lightweight German 49M (vosk-model-small-de-zamia-0.3)" \
	"11"  "Lightweight French 39M (vosk-model-small-fr-pguyot-0.3)" \
	"12"  "Lightweight Spanish 33M (vosk-model-small-es-0.3)" \
	"13"  "Lightweight Portuguese 31M (vosk-model-small-pt-0.3)" \
	"14"  "Generic Greek 1.1G (vosk-model-el-gr-0.6)" \
	"15"  "Lightweight Turkish 35M (vosk-model-small-tr-0.3)" \
	"16"  "Lightweight Vietnamese 32M (vosk-model-small-vn-0.3)" \
	"17"  "Speaker identification model 13M (vosk-model-spk-0.3)" \
	3>&1 1>&2 2>&3)

	case "${BOARD}" in
		"0")
			wget "https://alphacephei.com/kaldi/models/vosk-model-en-us-aspire-0.2.zip" -P "${TOP_DIR}"/models
			;;
		"1")
			source "${TOP_DIR}"/lib/H3SDK_BuildEnvironment.sh
			;;
		"2")
			source "${TOP_DIR}"/lib/H5SDK_BuildEnvironment.sh
			;;
		"3")
			source "${TOP_DIR}"/lib/A64SDK_BuildEnvironment.sh
			;;
		"4")
			source "${TOP_DIR}"/lib/H6SDK_BuildEnvironment.sh
			;;
		"6")
			wget "https://alphacephei.com/kaldi/models/vosk-model-small-ru-0.4.zip" -P "${MODELS_DIR}"
			unzip "${MODELS_DIR}"/vosk-model-small-ru-0.4.zip -d "${MODELS_DIR}"
			mv "${MODELS_DIR}"/vosk-model-small-ru-0.4 "${MODELS_DIR}"/sml-ru
			rm "${MODELS_DIR}"/vosk-model-small-ru-0.4.zip
			;;
		"20" | "21") #RDA 
			source "${TOP_DIR}"/lib/RDASDK_BuildEnvironment.sh
			;;
		"22") #3G-IOT
			source "${TOP_DIR}"/lib/3G-iotSDK_BuildEnvironment.sh
			;;
		"23") #4G-IOT
			source "${TOP_DIR}"/lib/4G-iotSDK_BuildEnvironment.sh
			;;
		*) # Other
    			echo "Unsupport Board!!!"
			;;
esac