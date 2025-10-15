import React, { useState, useEffect } from "react";
import Table from "./components/Table";
import Filters from "./components/Filters";
import Chart from "./components/Chart";
import loadData from "./lib/loadData";

type Book = {
  title: string;
  price: string;
  availability: string;
  rating: string;
  category: string;
  url: string;
};

export default function App() {
  const [books, setBooks] = useState<Book[]>([]);
  const [filter, setFilter] = useState("");

  useEffect(() => {
    loadData().then(setBooks);
  }, []);

  const filtered = books.filter(b =>
    b.title.toLowerCase().includes(filter.toLowerCase())
  );

  return (
    <div className="p-4 font-sans">
      <h1 className="text-xl font-bold mb-2">📚 Books to Scrape Viewer</h1>
      <Filters value={filter} onChange={setFilter} />
      <Chart data={filtered} />
      <Table data={filtered} />
    </div>
  );
}
