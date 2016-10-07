for flag in `ls -1 ./all-flags/`
do
    if [ ! -f ./flags/$flag ]; then
        echo $flag
        cp ./all-flags/$flag ./unused/
    fi
done
