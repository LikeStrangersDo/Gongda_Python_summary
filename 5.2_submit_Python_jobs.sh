#!/bin/bash

#################### Begin SLURM header ##########################
# Settings for the SLURM scheduler
#SBATCH -t 6:00:00 
#SBATCH --job-name TROPOMI_shipping_domain
#SBATCH --qos bblargemem
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=20G
####################  End SLURM header  ##########################
# load the Python packages needed (Python 3.8.6)

module purge; module load bluebear
module load bear-apps/2020b
module load IPython/7.18.1-GCCcore-10.2.0
module load SciPy-bundle/2020.11-foss-2020b
module load netcdf4-python/1.5.5.1-foss-2020b
######################################################################################################################
# pick one job from the ones below by removing the "#"
# or edit a new job based on the examples
# but remember to edit the job name, time, cpu and mem accordingly for each run
# To avoid making too many rows, you can use a text editor to get rows for other jobs

# 2019
#python shipping_NO2_part1.py --domain AS --qa_flag 0.75 --start_date 20190101 --end_date 20190131 --month 201901 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2019/NO2_201901/"
#python shipping_NO2_part1.py --domain AS --qa_flag 0.75 --start_date 20190201 --end_date 20190228 --month 201902 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2019/NO2_201902/"
#python shipping_NO2_part1.py --domain AS --qa_flag 0.75 --start_date 20190301 --end_date 20190331 --month 201903 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2019/NO2_201903/"
#python shipping_NO2_part1.py --domain AS --qa_flag 0.75 --start_date 20190401 --end_date 20190430 --month 201904 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2019/NO2_201904/"
#python shipping_NO2_part1.py --domain AS --qa_flag 0.75 --start_date 20190501 --end_date 20190531 --month 201905 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2019/NO2_201905/"
#python shipping_NO2_part1.py --domain AS --qa_flag 0.75 --start_date 20190601 --end_date 20190630 --month 201906 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2019/NO2_201906/"
#python shipping_NO2_part1.py --domain AS --qa_flag 0.75 --start_date 20190701 --end_date 20190731 --month 201907 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2019/NO2_201907/"
#python shipping_NO2_part1.py --domain AS --qa_flag 0.75 --start_date 20190801 --end_date 20190831 --month 201908 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2019/NO2_201908/"
#python shipping_NO2_part1.py --domain AS --qa_flag 0.75 --start_date 20190901 --end_date 20190930 --month 201909 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2019/NO2_201909/"
#python shipping_NO2_part1.py --domain AS --qa_flag 0.75 --start_date 20191001 --end_date 20191031 --month 201910 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2019/NO2_201910/"
#python shipping_NO2_part1.py --domain AS --qa_flag 0.75 --start_date 20191101 --end_date 20191130 --month 201911 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2019/NO2_201911/"
#python shipping_NO2_part1.py --domain AS --qa_flag 0.75 --start_date 20191201 --end_date 20191231 --month 201912 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2019/NO2_201912/"

# 2020
#python shipping_NO2_part1.py --domain EU --qa_flag 0.75 --start_date 20200101 --end_date 20200131 --month 202001 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2020/NO2_202001/"
#python shipping_NO2_part1.py --domain EU --qa_flag 0.75 --start_date 20200201 --end_date 20200229 --month 202002 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2020/NO2_202002/"
#python shipping_NO2_part1.py --domain EU --qa_flag 0.75 --start_date 20200301 --end_date 20200331 --month 202003 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2020/NO2_202003/"
#python shipping_NO2_part1.py --domain EU --qa_flag 0.75 --start_date 20200401 --end_date 20200430 --month 202004 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2020/NO2_202004/"
#python shipping_NO2_part1.py --domain EU --qa_flag 0.75 --start_date 20200501 --end_date 20200531 --month 202005 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2020/NO2_202005/"
#python shipping_NO2_part1.py --domain EU --qa_flag 0.75 --start_date 20200601 --end_date 20200630 --month 202006 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2020/NO2_202006/"
#python shipping_NO2_part1.py --domain EU --qa_flag 0.75 --start_date 20200701 --end_date 20200731 --month 202007 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2020/NO2_202007/"
#python shipping_NO2_part1.py --domain EU --qa_flag 0.75 --start_date 20200801 --end_date 20200831 --month 202008 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2020/NO2_202008/"
#python shipping_NO2_part1.py --domain EU --qa_flag 0.75 --start_date 20200901 --end_date 20200930 --month 202009 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2020/NO2_202009/"
#python shipping_NO2_part1.py --domain EU --qa_flag 0.75 --start_date 20201001 --end_date 20201031 --month 202010 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2020/NO2_202010/"
#python shipping_NO2_part1.py --domain EU --qa_flag 0.75 --start_date 20201101 --end_date 20201130 --month 202011 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2020/NO2_202011/"
#python shipping_NO2_part1.py --domain EU --qa_flag 0.75 --start_date 20201201 --end_date 20201231 --month 202012 --data_directory "/rds/projects/2018/maraisea-glu-01/Study/Research_Data/TROPOMI/0_TROPOMI_NO2_raw/2020/NO2_202012/"
######################################################################################################################
######################################################################################################################

# Exit normally
exit 0
#EOC
