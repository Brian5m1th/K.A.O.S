import { Input } from "@/shared/ui/input";
import { Button } from "@/shared/ui/button";

interface Props {
  value: string;
  onChange: (value: string) => void;
  onConfirm: () => void;
  onCancel: () => void;
}

export function CustomModelInput({ value, onChange, onConfirm, onCancel }: Props) {
  return (
    <div className="flex gap-1">
      <Input
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder="Type any model name..."
        className="h-7 text-[11px] w-44"
        onKeyDown={(e) => {
          if (e.key === "Enter") onConfirm();
          if (e.key === "Escape") onCancel();
        }}
        autoFocus
      />
      <Button variant="secondary" size="sm" className="h-7 px-2 text-[10px]" onClick={onConfirm}>
        OK
      </Button>
    </div>
  );
}