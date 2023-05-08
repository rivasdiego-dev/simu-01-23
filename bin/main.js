import nodeList from "./data/nodeList-ex1.js";

import { getLocalK, getLocalB} from "./locals.js";
import pkg from "prompt-sync"
import yargs from "yargs"

// VARS
const prompt = pkg({ sigint: true });
let getLocals = true;
let userPrompt, indexNode1, indexNode2, indexNode3;

const options = yargs
 .usage("Usage: -k <global k value> \n       -q <global q value>")
 .option("k", { alias: "global-k", describe: "The global k given", type: "number", demandOption: true })
 .option("q", { alias: "global-q", describe: "The global q given", type: "number", demandOption: true })
 .argv;
const globalK = options.k
const globalQ = options.q

// MAIN

while (getLocals) {
    indexNode1 = prompt('Wich global is the local 1? ');
    indexNode2 = prompt('Wich global is the local 2? ');
    indexNode3 = prompt('Wich global is the local 3? ');
    
    
    console.log('\nLOCAL K:');
    console.log(getLocalK(globalK, nodeList[indexNode1-1],nodeList[indexNode2-1],nodeList[indexNode3-1]));
    
    console.log('\nLOCAL B:');
    console.log(getLocalB(globalQ, nodeList[indexNode1-1],nodeList[indexNode2-1],nodeList[indexNode3-1]));


        
    userPrompt = prompt('Again? ');
        if (userPrompt != 'y')
            getLocals = false;
}