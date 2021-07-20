const express = require('express');
const router = express.Router();

const mysqlConnection = require('../database');

router.get('/', (req, res) => {
    mysqlConnection.query('SELECT * FROM employees', (err, rows, fields) => {
        if (!err) {
            res.json(rows);
        }else{
            console.log(err);
        }
    })
})

router.get('/:id', (req, res) => {
    const idsql = req.params.id;
    mysqlConnection.query('SELECT * FROM employees WHERE id = ?', [idsql], (err, rows, fields) => {
        if (!err) {
            res.json(rows[0]);
        }else{
            console.log(err);
        }
    })
});

router.post('/add', (req, res) => {
    const { name, salary } = req.body;
    const queryInsert = 'INSERT INTO employees (`name`,`salary`) VALUES (?, ?);';

    mysqlConnection.query(queryInsert, [name, salary], (err, rows, fields)=>{
        if(!err){
            res.json({Status: 'Employee created successfully'});
        }else{
            console.log(err);
        }
    })
})

router.put('/update/:id', (req, res)=>{
    const { name, salary } = req.body;
    const idsql = req.params.id;
    const queryUpdate = 'UPDATE employees SET `name` = ?, `salary` = ? WHERE `id` = ?;';

    mysqlConnection.query(queryUpdate, [name, salary, idsql], (err, rows, fields)=>{
        if(!err){
            res.json({Status: 'Employee Updated successfullyy'});
        }else{
            console.log(err);
        }
    })
})

router.delete('/delete/:id', (req, res)=>{
    const idsql = req.params.id;
    const queryDelete = 'DELETE FROM employees WHERE id = ?;'

    mysqlConnection.query(queryDelete, [idsql], (err, rows, fields)=>{
        if(!err){
            res.json({Status: 'Employee Deleted successfully'});
        }else{
            console.log(err);
        }
    })
})
module.exports = router;