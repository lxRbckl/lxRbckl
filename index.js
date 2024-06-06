// < Project lxRbckl by Alex Arbuckle > //


// import <
import openai from './dist/openai.js';
import octokit from './dist/octokit.js';
import {

   dirSet,
   dirGet,
   dirDel,
   fileSet,
   fileGet,
   fileDel,
   getProjectPath

} from './dist/local.js';

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