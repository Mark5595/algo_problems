function getMaximumScoreHelper(arr, sum, score, odd) {
    if (arr.length == 0) {
       return 0;
    }
    const combiner = odd ? (b) => score + b : (b) => score - b;
    const leftRemovalScore = getMaximumScoreHelper(arr.slice(1), sum - arr[0], combiner(arr[0]), !odd);
    const rightRemovalScore = getMaximumScoreHelper(arr.slice(0, arr.length - 1), sum - arr[arr.length - 1], combiner(arr[0]), !odd);

    if (leftRemovalScore > rightRemovalScore) {
        return leftRemovalScore;
    } else {
        return rightRemovalScore;
    }
}


/*
 * Complete the 'getMaximumScore' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts INTEGER_ARRAY integerArray as parameter.
 */
function getMaximumScore(integerArray) {
    return getMaximumScoreHelper(integerArray, integerArray.reduce((acc, cur) => acc + cur, 0), 0, true );
}
