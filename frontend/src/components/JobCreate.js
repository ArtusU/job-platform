import { useContext, useState } from "react";
import { Formik, Field, Form } from "formik";
import axios from "axios";
import { API } from "../api";
import { AuthContext } from "../contexts/AuthContext";

export function JobCreate() {
  const [loading, setLoading] = useState(false);
  const {
    user: { token },
  } = useContext(AuthContext);

  function handleSubmit(values) {
    setLoading(true);
    axios
      .post(API.jobs.create, values, {
        headers: {
          Authorization: `Token ${token}`,
        },
      })
      .then((res) => {
        console.log(res.data);
      })
      .finally(() => {
        setLoading(false);
      });
  }

  return (
    <div>
      {loading && "Loading..."}
      <Formik
        initialValues={{
          title: "",
          company_name: "",
          company_website: "",
          location: "",
          salary: "",
        }}
        onSubmit={handleSubmit}
      >
        {({ errors, touched }) => (
          <Form>
            <Field name="title">
              {({ field, form }) => (
                <label className="mt-3 block">
                  <span className="text-gray-700">Title</span>
                  <input
                    {...field}
                    type="text"
                    className="
                                        mt-1
                                        block
                                        w-full
                                        rounded-md
                                        border-gray-300
                                        shadow-sm
                                        focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50
                                    "
                    placeholder="Software developer"
                    style={
                      form.touched.title && form.errors.title
                        ? { border: "2px solid var(--primary-red)" }
                        : null
                    }
                  />
                </label>
              )}
            </Field>

            <Field name="company_name">
              {({ field, form }) => (
                <label className="mt-3 block">
                  <span className="text-gray-700">Company Name</span>
                  <input
                    {...field}
                    type="text"
                    className="
                                        mt-1
                                        block
                                        w-full
                                        rounded-md
                                        border-gray-300
                                        shadow-sm
                                        focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50
                                    "
                    placeholder="Facebook"
                    style={
                      form.touched.company_name && form.errors.company_name
                        ? { border: "2px solid var(--primary-red)" }
                        : null
                    }
                  />
                </label>
              )}
            </Field>

            <Field name="company_website">
              {({ field, form }) => (
                <label className="mt-3 block">
                  <span className="text-gray-700">Company Website URL</span>
                  <input
                    {...field}
                    type="text"
                    className="
                                        mt-1
                                        block
                                        w-full
                                        rounded-md
                                        border-gray-300
                                        shadow-sm
                                        focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50
                                    "
                    placeholder="https://www..."
                    style={
                      form.touched.company_website &&
                      form.errors.company_website
                        ? { border: "2px solid var(--primary-red)" }
                        : null
                    }
                  />
                </label>
              )}
            </Field>

            <Field name="location">
              {({ field, form }) => (
                <label className="mt-3 block">
                  <span className="text-gray-700">Location</span>
                  <input
                    {...field}
                    type="text"
                    className="
                                        mt-1
                                        block
                                        w-full
                                        rounded-md
                                        border-gray-300
                                        shadow-sm
                                        focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50
                                    "
                    placeholder="California"
                    style={
                      form.touched.location && form.errors.location
                        ? { border: "2px solid var(--primary-red)" }
                        : null
                    }
                  />
                </label>
              )}
            </Field>

            <Field name="salary">
              {({ field, form }) => (
                <label className="mt-3 block">
                  <span className="text-gray-700">Salary</span>
                  <input
                    {...field}
                    type="number"
                    className="
                                        mt-1
                                        block
                                        w-full
                                        rounded-md
                                        border-gray-300
                                        shadow-sm
                                        focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50
                                    "
                    style={
                      form.touched.salary && form.errors.salary
                        ? { border: "2px solid var(--primary-red)" }
                        : null
                    }
                  />
                </label>
              )}
            </Field>

            <button
              type="submit"
              className="mt-3 bg-blue-100 rounded-md shadow-sm text-lg px-5 py-3 hover:bg-blue-200 "
            >
              Submit
            </button>
          </Form>
        )}
      </Formik>
    </div>
  );
}
