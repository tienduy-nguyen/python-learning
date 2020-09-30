# Useful Methods In ES6 JavaScript - part 1

## Table of contents
- [Useful Methods In ES6 JavaScript - part 1](#useful-methods-in-es6-javascript---part-1)
  - [Table of contents](#table-of-contents)
  - [How to hide all elements specified?](#how-to-hide-all-elements-specified)
  - [How to check if the element has the specified class?](#how-to-check-if-the-element-has-the-specified-class)
  - [How to toggle a class for an element?](#how-to-toggle-a-class-for-an-element)
  - [How to get the scroll position of the current page?](#how-to-get-the-scroll-position-of-the-current-page)
  - [How to smooth-scroll to the top of the page?](#how-to-smooth-scroll-to-the-top-of-the-page)
  - [How to check if the parent element contains the child element?](#how-to-check-if-the-parent-element-contains-the-child-element)
  - [How to check if the element specified is visible in the viewport?](#how-to-check-if-the-element-specified-is-visible-in-the-viewport)
  - [How to fetch all images within an elements?](#how-to-fetch-all-images-within-an-elements)
  - [How to figure out if the device is a mobile device or a desktop/laptop?](#how-to-figure-out-if-the-device-is-a-mobile-device-or-a-desktoplaptop)
  - [How to get the current URL?](#how-to-get-the-current-url)
  - [How to create an object containing the parameters of the current URL?](#how-to-create-an-object-containing-the-parameters-of-the-current-url)
  - [How to encode a set of form elements as an object?](#how-to-encode-a-set-of-form-elements-as-an-object)
  - [How to retrieve a set of properties indicated by the given selectors from an object?](#how-to-retrieve-a-set-of-properties-indicated-by-the-given-selectors-from-an-object)
  - [How to invoke the provided function after wait (in milliseconds)?](#how-to-invoke-the-provided-function-after-wait-in-milliseconds)
  - [How to trigger a specific event on a given element, optionally passing custom data?](#how-to-trigger-a-specific-event-on-a-given-element-optionally-passing-custom-data)
  - [How to remove an event listener from an element?](#how-to-remove-an-event-listener-from-an-element)
  - [How to get readable format of the given number of milliseconds?](#how-to-get-readable-format-of-the-given-number-of-milliseconds)
  - [How to get the difference (in days) between two dates?](#how-to-get-the-difference-in-days-between-two-dates)
  - [How to make a GET request to the passed URL?](#how-to-make-a-get-request-to-the-passed-url)
  - [How to make a POST request to the passed URL?](#how-to-make-a-post-request-to-the-passed-url)
  - [How to create a counter with the specified range, step and duration for the specified selector?](#how-to-create-a-counter-with-the-specified-range-step-and-duration-for-the-specified-selector)
  - [How to copy a string to the clipboard?](#how-to-copy-a-string-to-the-clipboard)
  - [How to find out if the browser tab of the page is focused?](#how-to-find-out-if-the-browser-tab-of-the-page-is-focused)
  - [How to create a directory, if it does not exist?](#how-to-create-a-directory-if-it-does-not-exist)



## How to hide all elements specified?

```js
const hide = (...el) => [...el].forEach(e => (e.style.display = 'none'));

// Example
hide(document.querySelectorAll('img')); // Hides all 

```



## How to check if the element has the specified class?
```js
const hasClass = (el, className) => el.classList.contains(className);

// Example
hasClass(document.querySelector('p.special'), 'special'); // true
```



## How to toggle a class for an element?

```js
const toggleClass = (el, className) => el.classList.toggle(className);

// Example
toggleClass(document.querySelector('p.special'), 'special'); 
// The paragraph will not have the 'special' class anymore
```



## How to get the scroll position of the current page?
```js
const getScrollPosition = (el = window) => ({
  x: el.pageXOffset !== undefined ? el.pageXOffset : el.scrollLeft,
  y: el.pageYOffset !== undefined ? el.pageYOffset : el.scrollTop
});

// Example
getScrollPosition(); // {x: 0, y: 200}
```


## How to smooth-scroll to the top of the page?
- If using CSS
  ```css
  html, body{
    scroll-behavior: smooth;
  }
  ```
- If using js
  ```js
  const scrollToTop = () => {
  const c = document.documentElement.scrollTop || document.body.scrollTop;
  if (c > 0) {
    window.requestAnimationFrame(scrollToTop);
    window.scrollTo(0, c - c / 8);
  }
  };

  // Example
  scrollToTop();
  ```


## How to check if the parent element contains the child element?

```js
const elementContains = (parent, child) => parent !== child && parent.contains(child);

// Examples
elementContains(document.querySelector('head'), document.querySelector('title')); 
// true
elementContains(document.querySelector('body'), document.querySelector('body')); // false
```


## How to check if the element specified is visible in the viewport?

```js
const elementIsVisibleInViewport = (el, partiallyVisible = false) => {
  const { top, left, bottom, right } = el.getBoundingClientRect();
  const { innerHeight, innerWidth } = window;
  return partiallyVisible
    ? ((top > 0 && top < innerHeight) || (bottom > 0 && bottom < innerHeight)) &&
        ((left > 0 && left < innerWidth) || (right > 0 && right < innerWidth))
    : top >= 0 && left >= 0 && bottom <= innerHeight && right <= innerWidth;
};

// Examples
elementIsVisibleInViewport(el); // (not fully visible)
elementIsVisibleInViewport(el, true); // (partially visible)
```

## How to fetch all images within an elements?

```js
const getImages = (el, includeDuplicates = false) => {
  const images = [...el.getElementsByTagName('img')].map(img => img.getAttribute('src'));
  return includeDuplicates ? images : [...new Set(images)];
};

// Examples
getImages(document, true); // ['image1.jpg', 'image2.png', 'image1.png', '...']
getImages(document, false); // ['image1.jpg', 'image2.png', '...']
```

## How to figure out if the device is a mobile device or a desktop/laptop?

```js
const detectDeviceType = () =>
  /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)
    ? 'Mobile'
    : 'Desktop';

// Example
detectDeviceType(); // "Mobile" or "Desktop"
```


## How to get the current URL?

```js
const currentURL = () => window.location.href;

// Example
currentURL(); // 'https://google.com'
```

## How to create an object containing the parameters of the current URL?

```js
const getURLParameters = url =>
  (url.match(/([^?=&]+)(=([^&]*))/g) || []).reduce(
    (a, v) => ((a[v.slice(0, v.indexOf('='))] = v.slice(v.indexOf('=') + 1)), a),
    {}
  );

// Examples
getURLParameters('http://url.com/page?n=Adam&s=Smith'); // {n: 'Adam', s: 'Smith'}
getURLParameters('google.com'); // {}
```

## How to encode a set of form elements as an object?

```js
const formToObject = form =>
  Array.from(new FormData(form)).reduce(
    (acc, [key, value]) => ({
      ...acc,
      [key]: value
    }),
    {}
  );

// Example
formToObject(document.querySelector('#form')); // { email: 'test@email.com', name: 'Test Name' }
```

## How to retrieve a set of properties indicated by the given selectors from an object?

```js
const get = (from, ...selectors) =>
  [...selectors].map(s =>
    s
      .replace(/\[([^\[\]]*)\]/g, '.$1.')
      .split('.')
      .filter(t => t !== '')
      .reduce((prev, cur) => prev && prev[cur], from)
  );
const obj = { selector: { to: { val: 'val to select' } }, target: [1, 2, { a: 'test' }] };

// Example
get(obj, 'selector.to.val', 'target[0]', 'target[2].a'); // ['val to select', 1, 'test']
```


## How to invoke the provided function after wait (in milliseconds)?

```js
const delay = (fn, wait, ...args) => setTimeout(fn, wait, ...args);
delay(
  function(text) {
    console.log(text);
  },
  1000,
  'later'
); 

// Logs 'later' after one second.
```

## How to trigger a specific event on a given element, optionally passing custom data?

```js
const triggerEvent = (el, eventType, detail) =>
  el.dispatchEvent(new CustomEvent(eventType, { detail }));

// Examples
triggerEvent(document.getElementById('myId'), 'click');
triggerEvent(document.getElementById('myId'), 'click', { username: 'bob' });
```

## How to remove an event listener from an element?
```js
const off = (el, evt, fn, opts = false) => el.removeEventListener(evt, fn, opts);

const fn = () => console.log('!');
document.body.addEventListener('click', fn);
off(document.body, 'click', fn); // no longer logs '!' upon clicking on the page

```

## How to get readable format of the given number of milliseconds?
```js
const formatDuration = ms => {
  if (ms < 0) ms = -ms;
  const time = {
    day: Math.floor(ms / 86400000),
    hour: Math.floor(ms / 3600000) % 24,
    minute: Math.floor(ms / 60000) % 60,
    second: Math.floor(ms / 1000) % 60,
    millisecond: Math.floor(ms) % 1000
  };
  return Object.entries(time)
    .filter(val => val[1] !== 0)
    .map(([key, val]) => `${val} ${key}${val !== 1 ? 's' : ''}`)
    .join(', ');
};

// Examples
formatDuration(1001); // '1 second, 1 millisecond'
formatDuration(34325055574); // '397 days, 6 hours, 44 minutes, 15 seconds, 574 milliseconds'
```

## How to get the difference (in days) between two dates?
```js
const getDaysDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / (1000 * 3600 * 24);

// Example
getDaysDiffBetweenDates(new Date('2017-12-13'), new Date('2017-12-22')); // 9
```
## How to make a GET request to the passed URL?

```js
const httpGet = (url, callback, err = console.error) => {
  const request = new XMLHttpRequest();
  request.open('GET', url, true);
  request.onload = () => callback(request.responseText);
  request.onerror = () => err(request);
  request.send();
};

httpGet(
  'https://jsonplaceholder.typicode.com/posts/1',
  console.log
); 

// Logs: {"userId": 1, "id": 1, "title": "sample title", "body": "my text"}
```


## How to make a POST request to the passed URL?

```js
const httpPost = (url, data, callback, err = console.error) => {
  const request = new XMLHttpRequest();
  request.open('POST', url, true);
  request.setRequestHeader('Content-type', 'application/json; charset=utf-8');
  request.onload = () => callback(request.responseText);
  request.onerror = () => err(request);
  request.send(data);
};

const newPost = {
  userId: 1,
  id: 1337,
  title: 'Foo',
  body: 'bar bar bar'
};
const data = JSON.stringify(newPost);
httpPost(
  'https://jsonplaceholder.typicode.com/posts',
  data,
  console.log
); 

// Logs: {"userId": 1, "id": 1337, "title": "Foo", "body": "bar bar bar"}
```

## How to create a counter with the specified range, step and duration for the specified selector?

```js
const counter = (selector, start, end, step = 1, duration = 2000) => {
  let current = start,
    _step = (end - start) * step < 0 ? -step : step,
    timer = setInterval(() => {
      current += _step;
      document.querySelector(selector).innerHTML = current;
      if (current >= end) document.querySelector(selector).innerHTML = end;
      if (current >= end) clearInterval(timer);
    }, Math.abs(Math.floor(duration / (end - start))));
  return timer;
};

// Example
counter('#my-id', 1, 1000, 5, 2000); // Creates a 2-second timer for the element with id="my-id"
```

## How to copy a string to the clipboard?

```js
const copyToClipboard = str => {
  const el = document.createElement('textarea');
  el.value = str;
  el.setAttribute('readonly', '');
  el.style.position = 'absolute';
  el.style.left = '-9999px';
  document.body.appendChild(el);
  const selected =
    document.getSelection().rangeCount > 0 ? document.getSelection().getRangeAt(0) : false;
  el.select();
  document.execCommand('copy');
  document.body.removeChild(el);
  if (selected) {
    document.getSelection().removeAllRanges();
    document.getSelection().addRange(selected);
  }
};

// Example
copyToClipboard('Lorem ipsum'); // 'Lorem ipsum' copied to clipboard.
```


## How to find out if the browser tab of the page is focused?
```js
const isBrowserTabFocused = () => !document.hidden;

// Example
isBrowserTabFocused(); // true
```

## How to create a directory, if it does not exist?
```js
const fs = require('fs');
const createDirIfNotExists = dir => (!fs.existsSync(dir) ? fs.mkdirSync(dir) : undefined);

// Example
createDirIfNotExists('test'); // creates the directory 'test', if it doesn't exist
```

**[Source](https://dev.to/madarsbiss/20-modern-es6-snippets-to-solve-practical-js-problems-3n83)**