// < Project lxRbckl by Alex Arbuckle > //


// import <
import openai from './dist/src/openai.js';
import octokit from './dist/src/octokit.js';
import {

   dirSet,
   dirGet,
   dirDel,
   fileSet,
   fileGet,
   fileDel,
   getProjectPath

} from './dist/src/local.js';

// >


// export <
module.exports = {

   openai,
   octokit,

   dirSet,
   dirGet,
   dirDel,
   fileSet,
   fileGet,
   fileDel,
   getProjectPath

};

// >