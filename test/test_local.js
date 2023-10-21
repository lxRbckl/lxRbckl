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

      const result = await fileSet({

         pData : 'test',
         pFile : gFileTXT

      });
      assert.strictEqual(result, undefined);

   });
   it('can write to JSON files', async () => {

      const result = await fileSet({

         pFile : gFileJSON,
         pData : {"test" : "test"}

      });
      assert.strictEqual(result, undefined);

   });
   it('can prevent writing broken data.', async () => {

      const expected = 'Could not write to file.';
      const result = await fileSet({

         pFile : gFileJSON,
         pData : undefined

      });
      assert.strictEqual(result, expected);

   });

});


describe('fileGet() Test Suite', async () => {

   it('can read TXT files', async () => {

      const expected = 'test';
      const result = await fileGet({pFile : gFileTXT});
      assert.strictEqual(result, expected);

   });
   it('can read JSON files', async () => {

      const expected = {'test' : 'test'};
      const result = await fileGet({pFile : gFileJSON});
      assert.deepEqual(result, expected);

   });
   it('can detect invalid filepaths', async () => {

      const expected = 'Could not read file.';
      const result = await fileGet({pFile : 'dne.txt'});
      assert.strictEqual(result, expected);

   });

});


describe('fileDel() Test Suite', async () => {

   it('can delete TXT files', async () => {

      const result = await fileDel({pFile : gFileTXT});
      assert.strictEqual(result, undefined);

   });
   it('can delete JSON files', async() => {

      const result = await fileDel({pFile : gFileJSON});
      assert.strictEqual(result, undefined);

   });
   it('can delete invalid files', async () => {

      const expected = 'File does not exist.';
      const result = await fileDel({pFile : 'dne.txt'})
      assert.strictEqual(result, expected);

   });

});