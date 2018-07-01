FILE_TO_TRY=$3
URL=$1
CHALLENGE_ID=$2
MORE_PARAMS=$4
FILE_TO_TRY_B64=${FILE_TO_TRY}.base64
cat $FILE_TO_TRY | base64 > $FILE_TO_TRY_B64
curl -H 'Content-Disposition: form-data; name="file"; filename="lamalama.jpeg"' -X POST $URL/api/challenges/$CHALLENGE_ID/solve/$MORE_PARAMS -d "@./$FILE_TO_TRY_B64"
