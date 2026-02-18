type CheckLevel = "CORRECT" | "ERROR" | "WARNING";

interface Check {
  level: CheckLevel;
  message: string;
}
