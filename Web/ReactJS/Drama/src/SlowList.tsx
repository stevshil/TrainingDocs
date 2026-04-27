type Props = {
  query: string;
};

export default function SlowList({ query }: Props) {
  // Simulate expensive computation
  const start = performance.now();
  while (performance.now() - start < 500) {} // 500ms block

  const items = Array.from({ length: 100 }, (_, i) => `${query} result ${i}`);

  return (
    <ul>
      {items.map((item) => (
        <li key={item}>{item}</li>
      ))}
    </ul>
  );
}
