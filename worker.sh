start_date=$1
end_date=$2

`pwd`/query.sh $start_date $end_date 1weeks 1days rthk_data local
`pwd`/query.sh $start_date $end_date 1days 1days rthk_data local
`pwd`/query.sh $start_date $end_date 1days 1days rthk_data greaterchina
`pwd`/query.sh $start_date $end_date 1days 1days rthk_data international
`pwd`/query.sh $start_date $end_date 1days 1days rthk_data local,international,greaterchina,finance,sport
`pwd`/query.sh $start_date $end_date 1weeks 1days rthk_data greaterchina
`pwd`/query.sh $start_date $end_date 1weeks 1days rthk_data international
`pwd`/query.sh $start_date $end_date 1weeks 1days rthk_data local,international,greaterchina,finance,sport
`pwd`/query.sh $start_date $end_date 2weeks 1days rthk_data local
`pwd`/query.sh $start_date $end_date 2weeks 1days rthk_data international
`pwd`/query.sh $start_date $end_date 2weeks 1days rthk_data greaterchina
`pwd`/query.sh $start_date $end_date 2weeks 1days rthk_data local,international,greaterchina,finance,sport
`pwd`/query.sh $start_date $end_date 1months 1days rthk_data local
`pwd`/query.sh $start_date $end_date 1months 1days rthk_data international
`pwd`/query.sh $start_date $end_date 1months 1days rthk_data greaterchina
# `pwd`/query.sh $start_date $end_date 1months 1days rthk_data local,international,greaterchina,finance,sport
# `pwd`/query.sh $start_date $end_date 1months 1days ceo_blog_data
# `pwd`/query.sh $start_date $end_date 1months 1days fso_blog_data
# `pwd`/query.sh $start_date $end_date 2weeks 1days ceo_blog_data
# `pwd`/query.sh $start_date $end_date 2weeks 1days fso_blog_data
# `pwd`/query.sh $start_date $end_date 1weeks 1days ceo_blog_data
# `pwd`/query.sh $start_date $end_date 1weeks 1days fso_blog_data
# `pwd`/query.sh $start_date $end_date 1days 1days ceo_blog_data
# `pwd`/query.sh $start_date $end_date 1days 1days fso_blog_data

python `pwd`/plot.py $end_date local
python `pwd`/plot.py $end_date international
python `pwd`/plot.py $end_date greaterchina
