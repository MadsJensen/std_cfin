
for sub in $(<subjects.txt)
do
    eval submit_to_cluster -q highmem.q -m $2 \"python $1 $sub\"
done
