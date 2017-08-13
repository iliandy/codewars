// https://www.codewars.com/kata/5279f6fe5ab7f447890006a7
function pickPeaks(arr) {
  var pos = [];
  var peaks = [];
  var len = arr.length;
  for (let i = 1; i < len - 1; i ++) {
    if (arr[i] > arr[i-1] && arr[i] > arr[i+1]) {
      peaks.push(arr[i]);
      pos.push(i);
    }
    else if (arr[i] > arr[i-1] && arr[i] === arr[i+1]) {
      for (let j = i+1; j < len; j++) {
        if (arr[j] > arr[i] || (arr[j] === arr[i] && j === len-1)){
          break;
        }
        if (arr[j] < arr[i]) {
          peaks.push(arr[i]);
          pos.push(i);
          break;
        }
      }
    }
  }
  return { 'pos': pos , 'peaks': peaks };
}
