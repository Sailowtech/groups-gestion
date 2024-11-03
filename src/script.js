function readCSV(file, callback) {
    /**
     * Read a csv file and return a set of emails.
     * @param {File} file - The csv file to read.
     * @param {Function} callback - The function to call with the set of emails.
     */
    const reader = new FileReader();
    reader.onload = function (event) {
        const text = event.target.result;
        const lines = text.split('\n');
        const emails = new Set();
        lines.forEach(line => {
            const columns = line.split(',');
            // We only want user emails, not group emails
            console.log(columns);
            if (columns[1] && columns[1] !== 'Member Email' && columns[3] === 'USER\r') {
                emails.add(columns[1].trim());
            }
        });
        console.log(emails);
        callback(emails);
    };
    reader.readAsText(file);
}

function computeDifference() {
    /**
     * Compute the difference between two csv files containing mail addresses and return a csv file with the difference.
     */
    const file1 = document.getElementById('file1').files[0];
    const file2 = document.getElementById('file2').files[0];
    const groupEmail = document.getElementById('emailInput').value;
    const output = document.getElementById('output');

    if (!file1 || !file2) {
        output.textContent = 'Please select both CSV files.';
        return;
    }

    readCSV(file1, emails1 => {
        readCSV(file2, emails2 => {
            const difference = [...emails1].filter(email => !emails2.has(email));
            output.textContent = 'Group Email [Required],Member Email\n' +
                difference.map(email => `${groupEmail}, ${email}`).join('\n');
        });
    });
}

function downloadOutput() {
    /**
     * Download the output as a csv file.
     */
    const output = document.getElementById('output');
    const blob = new Blob([output.textContent], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'output.csv';
    a.click();
}
