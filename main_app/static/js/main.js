const menuEl = document.getElementById('menu');
const hamburger = document.getElementById('hamburger');
const search = document.getElementById('search');
const searchBar = document.getElementById('search-bar');
const salary = document.getElementById('salary')

hamburger?.addEventListener('click', () => {
  menuEl.classList.toggle('hidden');
})

searchBar?.addEventListener('focusin', () => {
  search.classList.add('hidden')
})

searchBar?.addEventListener('focusout', () => {
  search.classList.remove('hidden')
})

salary?.toLocaleString('en', {useGrouping:true});
