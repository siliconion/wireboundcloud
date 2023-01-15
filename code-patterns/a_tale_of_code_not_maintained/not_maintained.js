function get_logs(dbName, uuid) {
    switch (dbName) {
        case 'A':
            db = get_database_conn_A()
            break
        case 'B':
            db =  get_database_conn_B()
            break
        case 'C':
            db = get_database_conn_C()
            break
        default:
            return null
            break
    }

    sql = `SELECT * FROM logs WHERE uuid = ${uuid}`
    db.query(sql, function(err, result) {
        if (err) throw err
        return result
    })
}