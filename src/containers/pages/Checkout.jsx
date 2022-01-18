import Layout from "../../hocs/Layout"
import { useState, useEffect } from "react";
import { connect } from "react-redux"
import { setAlert } from "../../redux/actions/alert";
import {
    remove_item,
    update_item,
    get_items,
    get_total,
    get_item_total
} from "../../redux/actions/cart";

import CartItem from "../../components/cart/CartItem";
import { Link, Navigate } from "react-router-dom";
import { get_shipping_options } from '../../redux/actions/shipping'

import { refresh } from "../../redux/actions/auth";

import {
    get_payment_total,
    get_client_token,
    process_payment
} from '../../redux/actions/payment';
import DropIn from 'braintree-web-drop-in-react';
import Loader from 'react-loader-spinner';
import { countries } from '../../helpers/fixedCountries'
import ShippingForm from "../../components/checkout/ShippingForm";

const Checkout = ({
    get_items,
    get_total,
    get_item_total,
    isAuthenticated,
    items,
    amount,
    compare_amount,
    total_items,
    remove_item,
    update_item,
    setAlert,
    get_shipping_options,
    shipping,
    refresh,
    get_payment_total,
    get_client_token,
    process_payment,
    user,
    clientToken,
    made_payment,
    loading,
    original_price,
    total_amount,
    total_compare_amount,
    estimated_tax,
    shipping_cost,
}) => {
    const [formData, setFormData] = useState({
        full_name: '',
        address_line_1: '',
        address_line_2: '',
        city: '',
        state_province_region: '',
        postal_zip_code: '',
        country_region: 'Peru',
        telephone_number: '',
        shipping_id: 0,
    });
    const [data, setData] = useState({
        instance: {}
    });

    const {
        full_name,
        address_line_1,
        address_line_2,
        city,
        state_province_region,
        postal_zip_code,
        country_region,
        telephone_number,
        shipping_id,
    } = formData;

    const buy = async e => {
        e.preventDefault();
        let nonce = await data.instance.requestPaymentMethod();
        
          process_payment(
              nonce,
              shipping_id,
              '',
              full_name,
              address_line_1,
              address_line_2,
              city,
              state_province_region,
              postal_zip_code,
              country_region,
              telephone_number
          );
        
    }

    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

    const [render, setRender] = useState(false);

    useEffect(() => {
        window.scrollTo(0, 0)
        get_shipping_options()
    }, [])

    useEffect(() => {
        window.scrollTo(0, 0);
        get_items()
        get_total()
        get_item_total()
    }, [render])


    useEffect(() => {
        get_client_token();
    }, [user]);
    useEffect(() => {
        get_payment_total(shipping_id, '');
    }, [shipping_id]);




    if (!isAuthenticated)
        return <Navigate to='/' />;
    const showItems = () => {
        return (
            <div>
                {
                    items &&
                    items !== null &&
                    items !== undefined &&
                    items.length !== 0 &&
                    items.map((item, index) => {
                        let count = item.count;
                        return (
                            <div key={index}>
                                <CartItem
                                    item={item}
                                    count={count}
                                    update_item={update_item}
                                    remove_item={remove_item}
                                    render={render}
                                    setRender={setRender}
                                    setAlert={setAlert}
                                />
                            </div>
                        );
                    })
                }
            </div>
        )
    }



  

    const renderShipping = () => {
        if (shipping && shipping !== null && shipping !== undefined) {
            return (
                <div className='mb-5'>
                    {
                        shipping.map((shipping_option, index) => (
                            <div key={index}>
                                <input
                                    onChange={e => onChange(e)}
                                    value={shipping_option.id}
                                    name='shipping_id'
                                    type='radio'
                                    required
                                />
                                <label className='ml-4'>
                                    {shipping_option.name} - ${shipping_option.price} ({shipping_option.time_to_delivery})
                                </label>
                            </div>
                        ))
                    }
                </div>
            );
        }
    };
    const renderPaymentInfo = () => {
        if (!clientToken) {
          if (!isAuthenticated) {
              <Link
                to="/login"
                className="w-full bg-gray-600 border border-transparent rounded-md shadow-sm py-3 px-4 text-base font-medium text-white hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-50 focus:ring-gray-500"
              >
                Login
              </Link>
          } else {
            <button
              className="w-full bg-indigo-600 border border-transparent rounded-md shadow-sm py-3 px-4 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-50 focus:ring-indigo-500"
            >
              <Loader
                type='Oval'
                color='#fff'
                height={20}
                widht={20}
              />
            </button>
          }
        } else {
          return (
            <>
              <DropIn
                options={{
                    authorization: clientToken,
                    paypal: {
                        flow: 'vault'
                    }
                }}
                onInstance={instance => (data.instance = instance)}
              />
              <div className="mt-6">
                {loading?<button
                  className="w-full bg-indigo-600 border border-transparent rounded-md shadow-sm py-3 px-4 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-50 focus:ring-indigo-500"
                >
                  <Loader
                    type='Oval'
                    color='#fff'
                    height={20}
                    widht={20}
                  />
                </button>:
                <button
                type="submit"
                className="w-full bg-green-600 border border-transparent rounded-md shadow-sm py-3 px-4 text-base font-medium text-white hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-50 focus:ring-green-500"
              >
                Place Order
              </button>}
              </div>
            </>
          )
        }
      }
      if (made_payment)
        return <Navigate to='/thankyou' />;


    return (
        <Layout>
            <div className="bg-white">
                <div className="max-w-2xl mx-auto pt-16 pb-24 px-4 sm:px-6 lg:max-w-7xl lg:px-8">
                    <h1 className="text-3xl font-extrabold tracking-tight text-gray-900 sm:text-4xl">Shopping Cart Items ({total_items})</h1>
                    <div className="mt-12 lg:grid lg:grid-cols-12 lg:gap-x-12 lg:items-start xl:gap-x-16">
                        <section aria-labelledby="cart-heading" className="lg:col-span-7">
                            <h2 id="cart-heading" className="sr-only">
                                Items in your shopping cart
                            </h2>

                            <ul className="border-t border-b border-gray-200 divide-y divide-gray-200">
                                {showItems()}
                            </ul>
                        </section>

                        {/* Order summary */}

                        <ShippingForm
                            full_name={full_name}
                            address_line_1={address_line_1}
                            address_line_2={address_line_2}
                            city={city}
                            state_province_region={state_province_region}
                            postal_zip_code={postal_zip_code}
                            telephone_number={telephone_number}
                            countries={countries}
                            onChange={onChange}
                            user={user}
                            renderShipping={renderShipping}
                            total_amount={total_amount}
                            total_compare_amount={total_compare_amount}
                            estimated_tax={estimated_tax}
                            shipping_cost={shipping_cost}
                            shipping_id={shipping_id}
                            shipping={shipping}
                            buy={buy}
                            renderPaymentInfo={renderPaymentInfo}


                        />
                        
                        
                    </div>


                </div>
            </div>
        </Layout>
    )
}
const mapStateToProps = state => ({
    isAuthenticated: state.Auth.isAuthenticated,
    items: state.Cart.items,
    amount: state.Cart.amount,
    compare_amount: state.Cart.compare_amount,
    total_items: state.Cart.total_items,
    shipping: state.Shipping.shipping,
    user: state.Auth.user,
    clientToken: state.Payment.clientToken,
    made_payment: state.Payment.made_payment,
    loading: state.Payment.loading,
    original_price: state.Payment.original_price,
    total_amount: state.Payment.total_amount,
    total_compare_amount: state.Payment.total_compare_amount,
    estimated_tax: state.Payment.estimated_tax,
    shipping_cost: state.Payment.shipping_cost,
})

export default connect(mapStateToProps, {
    get_items,
    get_total,
    get_item_total,
    remove_item,
    update_item,
    setAlert,
    get_shipping_options,
    refresh,
    get_payment_total,
    get_client_token,
    process_payment,
})(Checkout)