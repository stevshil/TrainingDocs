import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as yup from "yup";

const schema = yup.object({
  firstName: yup.string()
    .min(2, 'Too short'),
  lastName: yup.string()
    .min(2, 'Too short')
    .required('Last name required'),
  email: yup.string()
    .email('Invalid email format')
    .matches(/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/, 'Enter a valid email address')
    .required('Email address required'),
}).required();

function MyForm() {
  const { register, handleSubmit, reset, watch, formState: { errors } } = useForm({
    resolver: yupResolver(schema)
  });
  
  const firstName = watch("firstName", "");
  
  const onSubmit = (data) => {
    console.log(data);
    reset();
  }

  return (
  <>
  <form>
    <input {...register("firstName")} placeholder="First Name" />
    <div>{errors.firstName && errors.firstName.message}</div>
    <input {...register("lastName")} placeholder="Last Name" />
    <div>{errors.lastName && errors.lastName.message}</div>
    <input {...register("email", { required: "Email is required" })} placeholder="Email Address" />
    <div>Repeat FirstName: {firstName}</div>
    <div>{errors.email && errors.email.message}</div>
    <button onClick={handleSubmit(onSubmit)}>Submit</button>
  </form>
    </>
  );
}

export default MyForm;