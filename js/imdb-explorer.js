/* Published snapshot aggregates only. The results table is the no-JS fallback. */
(() => {
  'use strict';
  const root = document.getElementById('vote-explorer');
  const source = document.getElementById('vote-floor-data');
  if (!root || !source) return;

  const data = JSON.parse(source.textContent);
  const rows = new Map(data.thresholds.map(row => [String(row.votes), row]));
  const number = new Intl.NumberFormat('en-US');
  const percent = value => `${(value * 100).toFixed(1)}%`;
  const setText = (id, value) => { document.getElementById(id).textContent = value; };

  function render(votes) {
    const row = rows.get(votes);
    if (!row) return;
    setText('explorer-titles', number.format(row.titles));
    setText('explorer-retained', percent(row.retained));
    setText('explorer-rating', row.mean_rating.toFixed(3));
    setText('explorer-documentary', percent(row.documentary_share));
    setText('explorer-action', percent(row.action_share));
    setText('explorer-shortlist', `${row.top50_retained} / 50`);
    document.getElementById('explorer-bar').style.width = `${row.retained * 100}%`;
    setText('explorer-summary',
      `At ${number.format(row.votes)} votes, ${number.format(row.titles)} movies remain eligible. ` +
      `${percent(1 - row.retained)} of the baseline catalogue is excluded; ` +
      `${row.top50_retained} of the original top 50 titles remain in the shortlist.`);
  }

  root.addEventListener('change', event => {
    if (event.target.matches('input[name="vote-floor"]')) render(event.target.value);
  });
  render(root.querySelector('input[name="vote-floor"]:checked').value);
  root.hidden = false;
})();
