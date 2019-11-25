// Roman to Integer

const symbolToValue = {
  'I' : 1,
  'V' : 5,
  'X' : 10,
  'L' : 50,
  'C' : 100,
  'D' : 500,
  'M' : 1000,
}

const isSubstractionPair = (left, right) => {
  if (left === 'I' && (right === 'V' || right === 'X')) {
    return true;
  } else if (left === 'X' && (right === 'L' || right === 'C')) {
    return true;
  } else if (left === 'C' && (right === 'D' || right === 'M')) {
    return true;
  } else {
    return false;
  }
}

const evaluateSubtractionPair = (left, right) => {
  const leftValue = symbolToValue[left];
  const rightValue = symbolToValue[right];
  return rightValue - leftValue;
}

const romanListToInt = (los) => {
  if (los.length >= 2 && isSubstractionPair(los[0], los[1])) {
    return evaluateSubtractionPair(los[0], los[1]) + romanListToInt(los.slice(2));
  } else if (los.length  >= 1) {
    return symbolToValue[los[0]] + romanListToInt(los.slice(1));
  } else {
    return 0;
  }
}

/**
 * Converts a roman numeral repsentation to an integer
 * ASSUMES '' => 0
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
  return romanListToInt(s.split(''));
};

 //Definition for singly-linked list.
 function ListNode(val) {
     this.val = val;
     this.next = null;
 }

// https://leetcode.com/problems/add-two-numbers/
const app = (cur, prev) => {
  const temp = new ListNode(cur);
  temp.next = prev
  return temp
}

const needCarry = (num) => Math.floor(num / 10) === 1

const addTwoNumbersHelp = (l1, l2, shouldCarry) => {
  if (l1 === null && l2 === null) {
    if (shouldCarry) {
      return new ListNode(1);
    } else {
      return null;
    }
  } else if (l1 === null) {
    if (shouldCarry) {
      return app((l2.val + 1) % 10, addTwoNumbersHelp(null, l2.next, needCarry(l2.val + 1)))
    } else {
      return app(l2.val, addTwoNumbersHelp(null, l2.next, 0))
    }
  } else if (l2 === null) {
    if (shouldCarry) {
      return app((l1.val + 1) % 10, addTwoNumbersHelp(l1.next, null, needCarry(l1.val + 1)))
    } else {
      return app(l1.val, addTwoNumbersHelp(l1.next, null, 0))
    }
  } else {
    if (shouldCarry) {
      return app((l1.val + l2.val + 1) % 10, addTwoNumbersHelp(l1.next, l2.next, needCarry(l1.val + l2.val + 1)))
    } else {
      return app((l1.val + l2.val) % 10, addTwoNumbersHelp(l1.next, l2.next, needCarry(l1.val + l2.val)))
    }
  }
}

 /**
  * @param {ListNode} l1
  * @param {ListNode} l2
  * @return {ListNode}
  */
 var addTwoNumbers = function(l1, l2) {
   return addTwoNumbersHelp(l1, l2, false)
 };

 /**
  * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
  * Output: 7 -> 0 -> 8
  * Explanation: 342 + 465 = 807.
  */
