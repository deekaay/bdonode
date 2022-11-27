const nodes = require('../data/exploration');
const links = require('../data/links');

nodeIds = Object.keys(nodes);

const maxCost = 100;
const numIterations = 100000;

const eligibleNodes = nodeIds.filter(x => {if (nodes[x] && (nodes[x].CP > 0  || nodes[x].kind == 2 )) return true; return false; });
console.log("id,name,cp");
eligibleNodes.forEach(x => console.log(nodes[x].key + "," + nodes[x].name + "," + nodes[x].CP ));
