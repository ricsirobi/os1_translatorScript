#!/bin/bash

help()
{
echo "Használati útmutató:
Leírás:
	Lefordít egy adott szöveget megadott nyelvről a másik megadott nyelvre
	-f
	    (from) nyelv, amiről fordítunk: két karakter, pl hu, en, es
	-t
	     (to) nyelv, amire fordítunk: két karakter, pl hu, en, es
	-w
	   (var/string) a szöveg amit szeretnénk lefordítani
	-h
	    (help) használati útmutató
   Használat:
	./shellscript.sh f hu t en szia
"; }

mytarget=""
mysource=""
myword=""

while getopts ":s:t:w:" opt; do
  case ${opt} in
    s)
	mysource=$OPTARG
	;;
    t)
	mytarget=$OPTARG
	;;
    w)
    myword=$OPTARG
	python3 -c "import translator; translator.csinald('$mysource', '$mytarget','$myword')";
	;;
    h)
	help
	exit
	;;
    *)
      help
      exit
      ;;
  esac
done

shift $((OPTIND -1))