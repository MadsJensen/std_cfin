subjects = $1

if [ $# == 2 ]
  then
    for sub in $(<subjects)
    do
        eval submit_to_cluster -q $3 -n 2 \"python $2 $sub\"
    done

elif [ $# == 3 ]
  then
    for sub in $(<subjects)
    do
        eval submit_to_cluster -q $3 -n $4  \"python $2 $sub\"
    done

elif [ $# == 4 ]
  then
    for sub in $(<subjects)
    do
        eval submit_to_cluster -q $3 -n $4  \"python $2 $sub $5\"
    done

else
    for sub in $(<subjects)
    do
        eval submit_to_cluster -n 2 \"python $2 $sub\"
    done

fi
