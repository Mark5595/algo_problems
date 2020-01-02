// 364. Nested List Weight Sum II

/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * function NestedInteger() {
 *
 *     Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     @return {boolean}
 *     this.isInteger = function() {
 *         ...
 *     };
 *
 *     Return the single integer that this NestedInteger holds, if it holds a single integer
 *     Return null if this NestedInteger holds a nested list
 *     @return {integer}
 *     this.getInteger = function() {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a single integer equal to value.
 *     @return {void}
 *     this.setInteger = function(value) {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
 *     @return {void}
 *     this.add = function(elem) {
 *         ...
 *     };
 *
 *     Return the nested list that this NestedInteger holds, if it holds a nested list
 *     Return null if this NestedInteger holds a single integer
 *     @return {NestedInteger[]}
 *     this.getList = function() {
 *         ...
 *     };
 * };
 */

// function accepts a nestedinteger and the depth.
const getMaxDepthHelp = (nl) => {
    if (!nl) {
        return 0;
    } else if (nl.isInteger()) {
        return 1;
    } else {
        return 1 + getMaxDepth(nl.getList());
    }
}

const getMaxDepth = (nl) => nl.reduce((a, c) => Math.max(a, getMaxDepthHelp(c)), 0);

const computeWeightHelp = (nl, depth) => {
    if (!nl) {
        return 0;
    } else if (nl.isInteger()) {
        return nl.getInteger() * depth;
    } else {
        return computeWeight(nl.getList(), depth - 1);
    }
}

const computeWeight = (nl, depth) => nl.reduce((a, c) => a + computeWeightHelp(c, depth), 0);

/**
 * @param {NestedInteger[]} nestedList
 * @return {number}
 */
var depthSumInverse = function(nestedList) {
    const maxDepth = getMaxDepth(nestedList);
    return computeWeight(nestedList, maxDepth)
};
