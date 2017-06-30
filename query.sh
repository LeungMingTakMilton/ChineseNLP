start_date=$1
end_date=$2
grep_interval=$3
shift_interval=$4
table=$5

if [ $# -ne 5 ]; then 
    category=$6
fi

while [ `date -d $end_date +"%Y%m%d"` -ge `date -d $start_date +"%Y%m%d"` ];
do
    outpath="data/output/$start_date/$grep_interval/$table/$category/"
    # 1days alignment in grep_date is for corntab working at 23:45
    grep_date=`date --date="$start_date $grep_interval ago 1days" +"%Y/%m/%d"`
    if [ $# -ne 5 ]; then
        echo "python sql.py -c $category $table $grep_date $start_date $outpath"
        python sql.py -c $category $table $grep_date $start_date $outpath
    else
        echo "python sql.py $table $grep_date $start_date $outpath"
        python sql.py $table $grep_date $start_date $outpath
    fi 
    start_date=`date --date="$start_date $shift_interval" +"%Y/%m/%d"`
        
done
