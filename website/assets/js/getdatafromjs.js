function getDataFromJS(table, key, col_name) {
    let col_index = table.columns.indexOf(col_name);
    let key_index = table.index.indexOf(key);
    return table.data[key_index][col_index];

}