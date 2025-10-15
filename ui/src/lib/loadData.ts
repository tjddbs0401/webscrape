export default async function loadData() {
  const res = await fetch("/data/items.jsonl");
  const text = await res.text();
  return text
    .split("\n")
    .filter(Boolean)
    .map(line => JSON.parse(line));
}
