if [ $# == 2 ]
  then
    for sub in $(<$2)
    do
        eval submit_to_cluster -q $3 -n 2 \"python $1 $sub\"
    done

elif [ $# == 3 ]
  then
    for sub in $(<$2)
    do
        eval submit_to_cluster -q $3 -n $4  \"python $1 $sub\"
    done

elif [ $# == 4 ]
  then
    for sub in $(<$2)
    do
        eval submit_to_cluster -q $3 -n $4  \"python $1 $sub $5\"
    done

else
    for sub in $(<$2)
    do
        eval submit_to_cluster -n 2 \"python $1 $sub\"
    done

fi
