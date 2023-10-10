// import <
const assert = require('assert');

const {

   fileSet,
   fileGet,
   fileDel

} = require('../source/local.js');

// >


// declare <
var gFileTXT = 'test.txt'
var gFileJSON = 'test.json'

// >


describe('fileSet() Test Suite', async () => {

   it('can write to TXT files', async () => {

      const expected = 'Could not write to file.';
      const result = await fileSet({

         pData : 'test',
         pFile : gFileTXT

      });
      assert.strictEqual(result, expected);

   });

});