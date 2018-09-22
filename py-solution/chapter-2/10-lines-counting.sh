# Testing Shell Script for defining the spec of the python script

BASEDIR=$(dirname $(realpath "$0"))

hightemp_path=$(realpath $BASEDIR/../../fixtures/hightemp.txt)

echo $BASEDIR

echo $hightemp_path

resultValue=$(pipenv run python $(realpath $BASEDIR/10-lines-counting.py) $hightemp_path)

expectValue=$(cat $hightemp_path | wc -l)

if [ $resultValue = $expectValue ]; then
  echo "Testing Pass"
else
  echo "Testing Fail"
fi
