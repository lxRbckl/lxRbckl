// import <
const assert = require('assert');

const {

   fileSet,
   fileGet,
   fileDel,
   dirSet,
   dirGet,
   dirDel

} = require('../source/fp/local.js');

// >


// declare <
var gTestDir = 'testdir';
var gFileTXT = 'test.txt';
var gFileJSON = 'test.json';

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


   it('can detect invalid files', async () => {

      const expected = 'File does not exist.';
      const result = await fileDel({pFile : 'dne.txt'})
      assert.strictEqual(result, expected);

   });

});


describe('dirSet() Test Suite', async () => {

   it('can create directories', async () => {

      const result = await dirSet({pDir : gTestDir});
      assert.strictEqual(result, undefined);

   });


   it('can detect invalid directories', async () => {

      const expected = 'Could not create directory.';
      const result = await dirSet({pDir : 'dne/dne/dne'});
      assert.strictEqual(result, expected);

   });

});


// describe('dirGet() Test Suite', async () => {

//    it('can read valid directories', async () => {

//       const expected = [

//          'test_local.js',
//          'test_remote.js'

//       ];
//       const result = await dirGet({pDir : '/test'});
//       assert.deepStrictEqual(result, expected);
      
//    });


//    it('can detect invalid directories', async () => {

//       const expected = 'Directory does not exist.';
//       const result = await dirGet({pDir : '/dne'});
//       assert.strictEqual(result, expected);

//    });

// });


// describe('dirDel() Test Suite', async () => {

//    it('can delete valid directories', async () => {

//       const result = await dirDel({pDir : gTestDir});
//       assert.strictEqual(result, undefined);

//    });

   
//    it('can detect invalid directories', async () => {

//       const expected = 'Directory does not exist.';
//       const result = await dirDel({pDir : 'dne'});
//       assert.strictEqual(result, expected);

//    });

// });