'use strict';
document.getElementById('download-recovery').addEventListener('click', function () {
  const blob = new Blob([document.getElementById('recovery-record').value], {type: 'text/plain;charset=utf-8'});
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = 'AIRR-private-recovery.txt';
  link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
});
