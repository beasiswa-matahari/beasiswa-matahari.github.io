const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  await page.setViewport({ width: 400, height: 800 });
  await page.goto('http://localhost:8081/index.html');
  
  // click menu
  await page.click('.v2-menu-toggle');
  await page.waitForSelector('.v2-nav.is-open');
  
  // evaluate and click dropbtn
  await page.evaluate(() => {
    document.querySelector('.dropbtn').click();
  });
  
  // wait 1 sec
  await new Promise(r => setTimeout(r, 1000));
  
  // check computed style
  const styles = await page.evaluate(() => {
    const el = document.querySelector('.dropdown-content');
    const comp = window.getComputedStyle(el);
    const rect = el.getBoundingClientRect();
    return {
      display: comp.display,
      position: comp.position,
      top: comp.top,
      left: comp.left,
      width: comp.width,
      height: comp.height,
      rect: { top: rect.top, left: rect.left, bottom: rect.bottom, right: rect.right, width: rect.width, height: rect.height }
    };
  });
  
  console.log(JSON.stringify(styles, null, 2));
  
  await browser.close();
})();
