import React, { useEffect, useState } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);

  const buildUrl = (path) => {
    const codespace = process.env.REACT_APP_CODESPACE_NAME;
    const base = codespace
      ? `https://${codespace}-8000.app.github.dev`
      : 'http://localhost:8000';
    return `${base}${path}`;
  };

  const fetchData = () => {
    const url = process.env.REACT_APP_CODESPACE_NAME
      ? `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`
      : 'http://localhost:8000/api/users/';
    console.log('Fetching Users from:', url);
    setLoading(true);
    fetch(url)
      .then(res => res.json())
      .then(data => {
        console.log('Raw Users response:', data);
        const results = data && data.results ? data.results : data;
        const list = Array.isArray(results) ? results : (results ? [results] : []);
        setUsers(list);
        console.log('Fetched Users (normalized):', list);
      })
      .catch(err => console.error('Error fetching users:', err))
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    fetchData();
  }, []);

  const renderTable = (items) => {
    if (!items || items.length === 0) return <div className="text-muted">No users found.</div>;
    const cols = Object.keys(items[0]);
    return (
      <div className="table-responsive">
        <table className="table table-striped table-sm">
          <thead className="table-light">
            <tr>
              {cols.map(c => <th key={c}>{c}</th>)}
            </tr>
          </thead>
          <tbody>
            {items.map((it, i) => (
              <tr key={it.id || i}>
                {cols.map(col => (
                  <td key={col}>{typeof it[col] === 'object' ? JSON.stringify(it[col]) : String(it[col])}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  };

  return (
    <div className="card mb-4">
      <div className="card-header d-flex justify-content-between align-items-center">
        <h5 className="mb-0">Users</h5>
        <div>
          <button className="btn btn-sm btn-primary me-2" onClick={fetchData} disabled={loading}>
            {loading ? 'Loading...' : 'Refresh'}
          </button>
          <a className="btn btn-sm btn-outline-secondary" href="#" onClick={(e)=>e.preventDefault()}>Docs</a>
        </div>
      </div>
      <div className="card-body">
        {renderTable(users)}
      </div>
    </div>
  );
};

export default Users;
