// Rendered-page checks for covers, responsive cards and existing navigation.
const { chromium } = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');
(async () => {
  const browser = await chromium.launch({headless: true});
  fs.mkdirSync('cover-review', {recursive:true});
  try {
    for (const [label,width,height] of [['desktop',1440,1000],['mobile',390,844]]) {
      const page = await browser.newPage({viewport:{width,height}});
      // Test the local build; third-party analytics/widgets are outside this change.
      await page.route('**/*', route => new URL(route.request().url()).hostname === '127.0.0.1' ? route.continue() : route.abort());
      await page.goto('http://127.0.0.1:8765/', {waitUntil:'networkidle'});
      const visible = () => page.locator('.post-card:visible').count();
      assert.equal(await page.locator('.post-card').count(),12);
      assert.equal(await visible(),9);
      async function checkImages() {
        for (const img of await page.locator('.post-card:visible img').all()) {
          await img.scrollIntoViewIfNeeded();
          await img.evaluate(i => i.decode());
          assert.equal(await img.evaluate(i=>i.naturalWidth),1200);
          const box=await img.boundingBox();
          assert.ok(Math.abs(box.width/box.height-1200/630)<0.01);
        }
        assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);
      }
      await checkImages();
      await page.screenshot({path:`cover-review/${label}-page-1.png`,fullPage:true});
      await page.locator('#yc-page-next').click();
      assert.equal(await visible(),3);
      await checkImages();
      await page.screenshot({path:`cover-review/${label}-page-2.png`,fullPage:true});
      await page.locator('[data-group="section"] [data-value="Casos de estudio"]').click();
      assert.equal(await visible(),2);
      await page.locator('#reset-filters').click();
      await page.locator('[data-group="section"] [data-value="Comunidad YaskCode"]').click();
      assert.equal(await visible(),3);
      await page.locator('#reset-filters').click();
      await page.locator('#article-search').fill('Hugging Face');
      assert.equal(await visible(),1);
      await checkImages();
      await page.close();
      console.log(`OK: ${label}; images, proportion, overflow, pagination, filters and search`);
    }
  } finally { await browser.close(); }
})().catch(e=>{console.error(e);process.exitCode=1});
