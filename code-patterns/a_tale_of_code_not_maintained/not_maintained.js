function get_logs(dbName, uuid) {
    switch (dbName) {
        case 'A':
            // TODO MIGRATE TO API
            db = get_database_conn_A()
            break
        case 'B':
            return call_service_B_API(uuid)
        case 'C':
            // TODO MIGRATE TO API
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