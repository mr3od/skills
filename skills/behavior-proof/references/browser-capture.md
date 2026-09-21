# Browser capture

Settings that make a screenshot or a video honest. Playwright is assumed; the ideas carry to any driver.

- Set capture conditions before navigating. `page.emulateMedia({ reducedMotion: 'reduce' })` applies to the next navigation, not the open document, and a reload after it applies again.
- A screenshot needs no injected CSS: `page.screenshot({ path, animations: 'disabled', caret: 'hide' })` disables animations, transitions and Web Animations for the shot and hides the caret.
- Video records the live page, so only there inject a motion-killing stylesheet, from an init script, guarded for a DOM that may not exist yet. An init script runs before the document's own scripts, and the driver does not surface what it throws.

```js
await page.addInitScript(() => {
    const killMotion = () => {
        const css = document.createElement('style');
        css.textContent = `*,*::before,*::after{animation:none!important;` +
            `transition:none!important;caret-color:transparent!important}`;
        (document.head ?? document.documentElement).appendChild(css);
    };
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', killMotion);
    } else {
        killMotion();
    }
});
```

- Playwright records VP8 WebM. GitHub accepts `.webm` and recommends H.264, so inline playback is not guaranteed; a transcoder such as `ffmpeg` fixes that, and `page.screencast` adds chapter cards and action callouts during the run. Report a missing tool as `blocked (tooling)`, named.
- Scroll a paginated or lazy list fully before concluding a row is absent. Where timing decides the result, force the timing rather than trusting the run to catch it.
