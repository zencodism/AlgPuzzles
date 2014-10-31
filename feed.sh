for i in `seq 1 10000`;
do
    tr -c -d 0-9 < /dev/urandom | head -c 10;
    echo; 
done

