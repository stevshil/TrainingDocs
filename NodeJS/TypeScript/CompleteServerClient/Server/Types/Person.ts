import { ObjectId } from "mongodb";

export interface Person {
  _id: ObjectId;
  name: string;
  hobbies?: string[];
  hobby?: string;
}
